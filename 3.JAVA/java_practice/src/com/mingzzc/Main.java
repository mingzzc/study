package com.mingzzc;


public class Main {

    //private static volatile boolean flag = false;

    public static void main(String[] args) throws InterruptedException {
        /*new Thread(new Runnable() {
            @Override
            public void run() {
                System.out.println("waiting data"+System.currentTimeMillis());
                while(!flag);
                System.out.println("============ success");
            }
        }).start();

        Thread.sleep(100);

        new Thread(new Runnable() {
            @Override
            public void run() {
                System.out.println("start--"+Thread.currentThread().toString());
                flag = true;

                System.out.println(System.currentTimeMillis()+"end--");
            }
        }).start();*/
        /*System.out.println("hello world");
        Thread thread = new Thread(new Runnable() {
            @Override
            public void run() {
                while (true) {
                    try {
                        Thread.sleep(1000);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                    System.out.println("running---");
                }
            }
        });
        thread.setDaemon(true);
        thread.start();
        System.out.println("???");
        thread.join();*/


        System.out.println(cups.B);

    }

    static class cup{
        public static int A = 2;

        static {
            A=3;
        }

        cup() {
            System.out.println("cup");
        }
    }

    static class cups extends cup{
        public static int B = A;

        static {
            B = 5;
        }
        cups() {
            System.out.println("cups");
        }
    }


}



