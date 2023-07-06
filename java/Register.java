import java.io.IOException;
import java.util.List;

public class Register {
	AccessMemberDB accessMemberDB = new AccessMemberDB("database.csv");
	List<Member> members;
	
	public boolean isMemberExist(String account) throws IOException {
		members = accessMemberDB.read();
		for(Member m : members) {
			if(m.getAccount().equals(account)) {
				return true;
			}
		}
		return false;
	}
	
	public boolean addMember(String account, String pwd) throws IOException {
		if(isMemberExist(account)) {
			return false;
		}else {
			accessMemberDB.write(new Member(account, pwd));
			return true;
		}
	}
	
}
