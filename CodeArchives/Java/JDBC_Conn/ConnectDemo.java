package JDBC_Conn;
import java.sql.*;


public class ConnectDemo {
    public static void main(String args[]) throws ClassNotFoundException, SQLException{
        Class.forName("com.mysql.jdbc.Driver");
        String url = "jdbc:mysql://localhost:3306/practice";
        String user = "root";
        String password = "sriram";
        Connection conn = DriverManager.getConnection(url, user, password);
        Statement st = conn.createStatement();
        
        String query = "select*from person";
        ResultSet rs = st.executeQuery(query);
        
        while(rs.next()){
            System.out.println(rs.getString(1)+rs.getString(1));
        }
    }
}
