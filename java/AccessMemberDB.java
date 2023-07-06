import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class AccessMemberDB {
	String filePath = "";
	String memberInDB;
	public AccessMemberDB(String filepath) {
		this.filePath = filepath;
	}
	
	public List<Member> read() throws IOException {
		List<Member> members = new ArrayList<Member>();
		File f = new File(filePath);
		if(!f.isFile()) {
			System.out.println("abc");
			//f.getParentFile().mkdirs();
			f.createNewFile();
		}
		BufferedReader reader = new BufferedReader(new FileReader(filePath));
		while((memberInDB = reader.readLine()) != null) {
			String[] membersInDB = memberInDB.split(",");
			members.add(new Member(membersInDB[0], membersInDB[1]));
		}
		reader.close();
		return members;
	}
	
	public void write(Member member) throws IOException {
		FileWriter writer = new FileWriter(filePath);
		
		writer.append(member.getAccount());
		writer.append(",");
		writer.append(member.getPwd());
		writer.append("\n");
		writer.flush();
		writer.close();
	}
}
