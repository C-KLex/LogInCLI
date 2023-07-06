import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Scanner;
import java.util.logging.FileHandler;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.logging.SimpleFormatter;

public class LoginCLI {
	private static Logger logger = Logger.getLogger(LoginCLI.class.getName());
	
	public static void main(String[] args) {
		Login login = new Login();
		Register register = new Register();
		
		try {
			FileHandler filehandler = new FileHandler("log.txt", true);
			//filehandler.setLevel(Level.INFO);
			filehandler.setFormatter(new SimpleFormatter());
			logger.addHandler(filehandler);
			logger.setUseParentHandlers(false);
			
			Scanner s = new Scanner(System.in);
			String isContinue = "9";
			while(isContinue.equals("9")) {
				isContinue = "";
				System.out.println("1. Login, 2. Register");
				String choise = s.nextLine();
	
				if(choise.equals("1")) {
					System.out.println("Please enter your account:");
					String account = s.nextLine();
					System.out.println("Please enter your password:");
					String pwd = s.nextLine();
					if(login.checkLogin(account, pwd)) {
						System.out.println("Login success.");
						logger.info("Login: \"Success\"; Account: \"" + account + "\"; Password: \"" + pwd + "\"");
					}else {
						System.out.println("Login failed.");
						logger.info("Login: \"Failed\"; Account: \"" + account + "\"; Password: \"" + pwd + "\"");
					}
				}else if(choise.equals("2")) {
					System.out.println("Please enter your account:");
					String account = s.nextLine();
					System.out.println("Please enter your password:");
					String pwd = s.nextLine();
					if(register.addMember(account, pwd)) {
						System.out.println("Register success.");
						logger.info("Register: \"Success\"; Account: \"" + account + "\"; Password: \"" + pwd + "\"");
					}else {
						System.out.println("Register failed, account already exist!");
						logger.info("Register: \"Failed\"; Account: \"" + account + "\"; Password: \"" + pwd + "\"");
					}
				}else {
					System.out.println("Your input is not 1 or 2!!!");
				}
				System.out.println("\nEnter 9 for restart, any other key for terminate!");
				isContinue = s.nextLine();
			}
			filehandler.close();
		}
		catch(FileNotFoundException e) {
			System.out.println("Database not found! \nPlease check if there is a database, "
					+ "or if the database is in the right place.");
		}
		catch(Exception e) {
			System.out.println("**You can ignore the NoSuchElement Exception if you just want to stop the login cli app.**");
			e.printStackTrace();
		}
	}
}
