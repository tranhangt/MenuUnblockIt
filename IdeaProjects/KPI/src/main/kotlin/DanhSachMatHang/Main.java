package DanhSachMatHang;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = Integer.parseInt(sc.nextLine());
        List<MatHang> ds = new ArrayList<>();
        for (int i = 1; i <= t; i++){
            ds.add(new MatHang(i, sc.nextLine(), sc.nextLine(), Integer.parseInt(sc.nextLine()), Integer.parseInt(sc.nextLine())));
        }
        Collections.sort(ds);
        for(MatHang mh: ds){
            System.out.println(mh);
        }
    }
}
