package optimización;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Archivos_AG1 {
    public String leertxt(String direccion){
        String txt="";
        try {
            Scanner s = new Scanner(new File(direccion));
            s.nextLine();
            while(s.hasNext()){
                txt+=s.nextLine();
            }
        } catch (FileNotFoundException ex) {
            Logger.getLogger(Archivos_AG1.class.getName()).log(Level.SEVERE, null, ex);
        }
        return txt;
    }
   
}