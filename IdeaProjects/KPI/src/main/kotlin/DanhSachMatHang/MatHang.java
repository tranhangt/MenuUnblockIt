package DanhSachMatHang;

public class MatHang implements Comparable<MatHang> {
    private String id, ten, donVi;
    private int mua, ban, loiNhuan;

    public MatHang(int id, String ten, String donVi, int mua, int ban) {
        this.id = "MH" + String.format("%03d", id);
        this.ten = ten;
        this.donVi = donVi;
        this.mua = mua;
        this.ban = ban;
        this.loiNhuan = ban - mua;
    }

    @Override
    public int compareTo(MatHang o) {
        if(loiNhuan <= o.loiNhuan) return 1;
        return -1;
    }

    @Override
    public String toString(){
        return id + " " + ten + " " + donVi + " " + mua + " " + ban + " " + loiNhuan;
    }
}
