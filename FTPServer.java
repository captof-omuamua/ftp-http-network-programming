import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.file.Files;
import java.nio.file.Paths;

public class FTPServer {
    private static final String FILE_DIRECTORY ="/home/LOCAL_USER/Downloads" ; // Specify the directory path here
    private static final String EOF_MARKER = "EOF_MARKER";

    public static void main(String[] args) {
        int port = 12345;
        try (ServerSocket serverSocket = new ServerSocket(port)) {
            System.out.println("Server is listening on port " + port);
            while (true) {
                Socket clientSocket = serverSocket.accept();
                System.out.println("Client connected: " + clientSocket.getInetAddress().getHostAddress());

                // Create input and output streams
                DataInputStream dis = new DataInputStream(clientSocket.getInputStream());
                DataOutputStream dos = new DataOutputStream(clientSocket.getOutputStream());

                // Read client request
                String fileName = dis.readUTF();
                String filePath = FILE_DIRECTORY + File.separator + fileName;

                // Check if file exists and has a valid .txt extension
                if (fileName.endsWith(".txt") && new File(filePath).exists()) {
                    dos.writeUTF("File found");

                    // Send file contents to client
                    try (BufferedReader br = Files.newBufferedReader(Paths.get(filePath))) {
                        String line;
                        while ((line = br.readLine()) != null) {
                            dos.writeUTF(line);
                        }
                        // Send EOF marker to indicate end of file
                        dos.writeUTF(EOF_MARKER);
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                } else if (!fileName.endsWith(".txt")) {
                    dos.writeUTF("Incorrect File Format");
                } else {
                    dos.writeUTF("Requested File Not Found");
                }

                // Close client connection
                clientSocket.close();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
