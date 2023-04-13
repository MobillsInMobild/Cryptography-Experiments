import java.io.*;
import java.util.BitSet;
import java.util.Scanner;
//埃拉托斯特尼筛法， static void sieceOfEratosthenes(long N) 可以对至多6000000000以内的数生成质数表。
public class SieveOfEratosthenes {
    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(System.in);
        System.out.println("Please input your N");
        long N = input.nextLong();
        sieceOfEratosthenes(N+1);
        System.out.println("\nThat's all");
    }

    static void sieceOfEratosthenes(long N) throws IOException {
        //bits1，bits2，bits3分别表示0~2000000000，2000000000~4000000000，4000000000~6000000000的位域
        BitSet bits1 = new BitSet(2000000000);
        BitSet bits2 = new BitSet(2000000000);
        BitSet bits3 = new BitSet(2000000000);
        bits1.set(0);
        bits1.set(2000000000);
        bits2.set(0);
        bits2.set(2000000000);
        bits3.set(0);
        bits3.set(2000000000);
        //用来标记输入N需要哪种位域
        boolean oneInt = false, twoInt = false;

        FileWriter f=new FileWriter("prime_table.txt");
        BufferedWriter os=new BufferedWriter(f);



        if (N > 2000000000) {
            oneInt = true;
            if (N - 2000000000 > 2000000000) {
                twoInt = true;
            }
        }

        for (int i = 2; i < Math.sqrt(N); i++) {
            if (bits1.get(i) == false) {
                for (long j = i; j < N / i + 1; j++) {
                    long ij = (long) i * j;
                    if (0 < ij && ij <= 2000000000) {
                        bits1.set(Math.toIntExact(ij));
                    } else if (2000000000 < ij && ij - 2000000000 <= 2000000000) {
                        bits2.set(Math.toIntExact(ij - 2000000000));
                    } else if (ij - 2000000000 > 2000000000) {
                        bits3.set(Math.toIntExact(ij - 2000000000 - 2000000000));
                    } else {
                        //超出位域，输出此时ij的值，用于调试
                        System.out.println(ij);
                    }
                }
            }
        }


        if (oneInt) {
            if (twoInt) {
                for (int i = 2; i < 2000000000; i++) {
                    if (!bits1.get(i)) {
                        //System.out.print(i + " ");
                        os.write(i+" ");
                    }
                }
                for (int i = 0; i < 2000000000; i++) {
                    if (!bits2.get(i)) {
                        //System.out.print((long)i + 2000000000 + " ");
                        os.write((long)i + 2000000000 + " ");
                    }
                }
                for (int i = 0; i < N - 2000000000 - 2000000000; i++) {
                    if (!bits3.get(i)) {
                        //System.out.print((long)i + 2000000000 + 2000000000 + " ");
                        os.write((long)i+2000000000 + 2000000000 +" ");
                    }
                }
            } else {
                for (int i = 2; i < 2000000000; i++) {
                    if (!bits1.get(i)) {
                        //System.out.print(i + " ");
                        os.write(i+" ");
                    }
                }
                for (int i = 0; i < N - 2000000000; i++) {
                    if (!bits2.get(i)) {
                        //System.out.print((long)i + 2000000000 + " ");
                        os.write((long)i + 2000000000 + " ");
                    }
                }
            }
        } else {
            for (int i = 2; i < N; i++) {
                if (!bits1.get(i)) {
                    //System.out.print(i + " ");
                    os.write(i+" ");
                }
            }
        }
        os.close();    }
}
