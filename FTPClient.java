import java.io.*;
import java.net.Socket;
import java.util.Scanner;

public class FTPClient {
    private static final String EOF_MARKER = "EOF_MARKER";

    public static void main(String[] args) {
        String serverAddress = "localhost";
        int port = 12345;

        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the filename to request from the server: ");
        String fileName = scanner.nextLine();

        try (Socket socket = new Socket(serverAddress, port)) {
            DataInputStream dis = new DataInputStream(socket.getInputStream());
            DataOutputStream dos = new DataOutputStream(socket.getOutputStream());

            // Send file request to server
            dos.writeUTF(fileName);

            // Receive response from server
            String response = dis.readUTF();
            if (response.equals("File found")) {
                System.out.println("File contents received from server:");
                String line;
                while (!(line = dis.readUTF()).equals(EOF_MARKER)) {
                    System.out.println(line);
                }
            } else {
                System.out.println("Server response: " + response);
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            scanner.close();
        }
    }
}
