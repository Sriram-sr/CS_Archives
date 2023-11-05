import java.sql.*;

public class ConnectDbDemo {
    public static void main(String args[]) throws Exception{
        String url = "jdbc:mysql://localhost:3306/practice";
        String user = "root";
        String password = "sriram";
// com.mysql.jdbc.Driver
        String query = "select*from person";
        Class.forName("com.mysql.jdbc.Driver");  //this registers class(driver)
        Connection conn = DriverManager.getConnection(url, user, password);
        Statement st = conn.createStatement();

        ResultSet rs = st.executeQuery(query);
        // System.out.println(rs.next());
        // rs.next();
        while(rs.next()){
            System.out.println(rs.getInt(1)+ " "+rs.getString(2)+" "+rs.getInt(3)+" "+rs.getString(4) );
        }
        // query = "insert into person values(7,'sRsds',22,'sdssaa','sadsdsdsdwsaa')";
        // int count = st.executeUpdate(query);
        // System.out.println(count + " rows affected");

        query = "delete from person where sno=7";
        int count = st.executeUpdate(query);
        System.out.println(count);
        st.close();
        conn.close();
    }
}
