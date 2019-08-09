import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
public class postgreConnectivity {
   public static void main(String args[]) {
      Connection c = null;
      try {
         Class.forName("org.postgresql.Driver");
         c = DriverManager
            .getConnection("jdbc:postgresql://tantor.db.elephantsql.com:5432/xnokayxj",
            "xnokayxj", "M_Pslc43o7UDPq5rTRc9WlQbFaEN4IEa");
      
      System.out.println("Opened database successfully");
      Statement stmt = c.createStatement();
      ResultSet tmp = stmt.executeQuery( "SELECT * FROM defaulters where paid='0'" );
      while ( tmp.next() ) {
    	  String noplate =tmp.getString("no_plate");
    	  String fault = tmp.getString("default_type");
    	  String place = tmp.getString("place");
    	  String fine = tmp.getString("fine");
    	  //$row[0],"fault"=>$row[1],"place"=>$row[2],"fine"=>$row[4],
    	  String mobile = tmp.getString("mobile");
    	  String mail = tmp.getString("email");
    	  String owner = tmp.getString("owner_name");
    	  String dati = tmp.getString("datetime");
    	  int id = tmp.getInt("id");
    	  testsms chk = new testsms();
    	  String msg="Kindly visit the link to pay your challan of amount"+fine+"\n"+"perseverancenitj.pythonanywhere.com";
    	  //System.out.println(chk.test(msg, mobile));
    	  //System.out.println("hello");
 	      TestMail.send("perseverancenitj@gmail.com","perseverance@nitj",mail,"e-challan",msg);
 	      PreparedStatement stmt1 = c.prepareStatement("Update defaulters set paid='1' where id=?");
	      stmt1.setInt(1, id);
	      stmt1.executeUpdate();
 	      //UpdatePaid.fun(id);
 	      // we have to get the input stream in order to actually send the request
 	      //con.getInputStream();
    	  //mobile"=>$row[6],"mail"=>$row[7],"owner"=>$row[8],"dati"=>$row[10]
      }
      tmp.close();
      stmt.close();
      c.close();

   
   } catch (Exception e) {
       e.printStackTrace();
       System.err.println(e.getClass().getName()+": "+e.getMessage());
       System.exit(0);
    }
   
   //System.out.println("Operation done successfully");
   }
}


