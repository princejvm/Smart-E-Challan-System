import java.util.Properties;    
import javax.mail.*;    
import javax.mail.internet.*;    
class TestMail{  
    public static void send(String from,String password,String to,String sub,String msg){  
          //Get properties object    
          Properties props = new Properties();    
          props.put("mail.smtp.host", "smtp.gmail.com");    
          props.put("mail.smtp.socketFactory.port", "465");    
          props.put("mail.smtp.socketFactory.class",    
                    "javax.net.ssl.SSLSocketFactory");    
          props.put("mail.smtp.auth", "true");    
          props.put("mail.smtp.port", "465"); 
          props.put("mail.smtp.starttls.enable","false");
          //get Session   
         // System.out.println("error");
   
          Session session = Session.getDefaultInstance(props, new javax.mail.Authenticator() {
        	    protected PasswordAuthentication getPasswordAuthentication() {
        	        return new PasswordAuthentication(from, password);
        	    }
        	});

          //System.out.println("hey error");
          //compose message    
          try {  
        	 
          // System.out.println("hi error");	  
           MimeMessage message = new MimeMessage(session);    
           message.addRecipient(Message.RecipientType.TO,new InternetAddress(to));    
           message.setSubject(sub);    
           message.setText(msg);    
           //send message  
           Transport.send(message);    
           System.out.println("message sent successfully");    
          } catch (MessagingException e) {System.out.println("mail me problem");}    
             
    }
 
}  
