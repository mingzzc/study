package com.mingzzc;


import java.util.HashMap;
import java.util.Map;

public class ClassLoaderTest {

    public static void main(String[] args) {
        int[][] p={{0,0},{4,5},{7,8},{8,9},{5,6},{3,4},{1,1}};
        System.out.println(maxPoints(p));
    }

    public static int maxPoints(int[][] points) {
        Map<Double,Integer> map = new HashMap<Double, Integer>();
        double rt;
        int num;
        for(int i=0;i<points.length;i++){
            for (int j=i+1;j<points.length;j++){
                if(points[j][0]-points[i][0]==0) {
                    rt = 100000;

                } else{
                    rt = (double)(points[j][1]-points[i][1])/(points[j][0]-points[i][0]);
                    rt=rt*1000000+(points[i][1]-rt*points[i][0]);
                }
                System.out.println(points[i][0]+" "+points[i][1]+" "+points[j][0]+" "+points[j][1]+" "+rt);
                if(map.containsKey(rt)) {
                    num = map.get(rt);
                    map.put(rt,num+1);
                } else {
                    map.put(rt, 1);
                }
            }
        }

        int ans = 0;
        for(double d:map.keySet()) {
            //System.out.println(d + "  " + map.get(d));
            ans=Math.max(ans, map.get(d));
        }
        return (int)Math.sqrt(2*ans)+1;
    }

    public int test(int x){
        int y=x*x;
        return y;
    }

    private int getSum() {
        int a=5;
        int b=10;
        return a+b;
    }

    public int testGetSum() {
         int i=getSum();
         return i;
    }

    public void add() {
        int i1=10;
        i1++;
        int i2=10;
        ++i2;
        int i3=0;
        i3=i1++;

        int i4=0;
        i4=++i2;


    }


}
