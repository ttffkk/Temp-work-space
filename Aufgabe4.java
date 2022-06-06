public class Aufgabe4{
    public static void main(String[] args){
        boolean[] b = new boolean[101];     //Array der die Zellen dastellen soll
        int d=2;
        while(d<=100){
        for(int i=0; i<b.length; i++){      //Schleife/Wärter , die die Zellen durchlaufen
            if(i%d==0){
                if(b[i]) {b[i]=false;}
                else{b[i]=true;}
            }
        }
        d++;
        }
        System.out.println("Geöffnete Türen:");
        for(int i=0; i<b.length; i++){
            if(b[i]){
                System.out.print(i+" ");
            }
        }
        System.out.println();
        System.out.println("Geschlossene Türen:");
        for(int i=0; i<b.length; i++){
            if(!b[i]){
                System.out.print(i+" ");
            }
        }
    }

    }