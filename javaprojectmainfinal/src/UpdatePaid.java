import java.io.IOException;
import java.io.PrintStream;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;

import org.postgresql.jdbc.PgStatement;

public class UpdatePaid {
	public static void fun(String id) {
		Connection c = null;
		try {
			Class.forName("org.postgresql.Driver");
			c = DriverManager.getConnection("jdbc:postgresql://tantor.db.elephantsql.com:5432/xnokayxj", "xnokayxj",
					"M_Pslc43o7UDPq5rTRc9WlQbFaEN4IEa");
			System.out.println("Opened database successfully");
			PreparedStatement stmt = c.prepareStatement("Update defaulters where id=?");
			stmt.setString(1, id);
			ResultSet tmp = stmt.executeQuery();

		} catch (Exception e) {
			System.out.println(e);
		}
		// for updating using php file
		try {
			URL url = new URL("https://wwwpersevarancecom.000webhostapp.com/updatePaid.php");
			URLConnection con = url.openConnection();
			// activate the output
			con.setDoOutput(true);
			PrintStream ps = new PrintStream(con.getOutputStream());
			// send your parameters to your site
			ps.print("&id=" + id);

			// we have to get the input stream in order to actually send the request
			con.getInputStream();

			// close the print stream
			ps.close();
		} catch (MalformedURLException e1) {
			e1.printStackTrace();
		} catch (IOException e2) {
			e2.printStackTrace();
		}

	}
}
