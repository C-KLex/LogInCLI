import java.io.IOException;
import java.util.List;

public class Login {
	AccessMemberDB accessMemberDB = new AccessMemberDB("database.csv");
	List<Member> members;
	
	public boolean checkLogin(String account, String pwd) throws IOException {
		members = accessMemberDB.read();
		for(Member m : members) {
			if(m.getAccount().equals(account) && m.getPwd().equals(pwd)) {
				return true;
			}
		}
		return false;
	}
}
