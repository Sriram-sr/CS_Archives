package JDBC_Conn;
import java.sql.*;

public class DbConnect {
    public static void main(String args[]) throws ClassNotFoundException, SQLException{
        String url = "jdbc:mysql://localhost:3306/practice";
        String user = "root";
        String password = "sriram";
        Class.forName("com.mysql.jdbc.Driver");
        Connection conn = DriverManager.getConnection(url, user, password);
        Statement st = conn.createStatement();
        String query = "insert into person values(4,'Swani',25,'cgk','Jani')";
        int status = st.executeUpdate(query);
        System.out.println(status);
        st.close();
        conn.close();
        // while(rs.next()){
        //     System.out.println(rs.getString(1)+" "+ rs.getString(2));
        // }
    }
}
