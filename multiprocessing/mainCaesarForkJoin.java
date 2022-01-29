/*----------------------------------------------------------------
 *
 * Proyecto final: Cifrado con algoritmo cesar
 * Fecha: 26-Nov-2017
 *
 *--------------------------------------------------------------*/

import java.util.concurrent.ForkJoinPool;

public class mainCaesarForkJoin{

	private static final int MAXTHREADS = Runtime.getRuntime().availableProcessors();

	public static void main(String[] args){
		ForkJoinPool pool; 
		double ms = 0.0;
		int N = 10, WHEEL = 25;
		String text = "";

		for(int i = 0 ; i < 10000 ; i++){
			text = text.concat("hola este texto esta cifrado con el algoritmo cesar ");
		}

		for (int k=0 ; k < N ; k++){
			double start = System.currentTimeMillis();
			for (int i = 0 ; i <= WHEEL ; i++){
				pool = new ForkJoinPool(MAXTHREADS);
				pool.invoke(new caesarForkJoin(text.toCharArray(),0,520000));
			}
			ms += System.currentTimeMillis() - start;
		}
		System.out.println("avg time = " + ms/(double)N +" ms");
	}
}