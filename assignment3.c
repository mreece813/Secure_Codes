#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
/* Michael Reece
 * 31/10/19
 * 177000762
 * Used Notes and Files from class and StackOverFlow */

void swap(int *a, int *b){
	/* This Function will swap the values in the array */
	int temp = *a;
	*a = *b;
	*b = temp;
}

void bubble_sort(int array[], int i){
	/* This will sort the array and if needed send the values to
	 * the swap function to swap the values.
	 * Uses the bool to be able to assign true and false	*/
	int a,b;
	bool swapped;
	for(a=0; a<i; a++){
		swapped = false;
		for(b=0; b<i-a; b++){
			if(array[b] > array[b+1]){
				swap(&array[b], &array[b+1]);
				swapped = true;
			}
		}
		if(swapped == false)
			break;	
	}
}

void print(int array[], int i){
	/* This will print out the sorted array by each index */
	int c;
	for(c=1; c<i; c++){
		printf("%i,",array[c]);
	}
	printf("%i ",array[10]);
	printf("\n");
}

int main()
{
	/* This Function has the User input the elements in the array and then will find the
	 * sum, average, and float average, then will send array to be sorted in bubble_sort */
	int x,i=10,sum=0,int_avg=0;
	float float_avg=0;

	int array[i];

	for(x=1; x<=i; x++){
		printf("Enter element %i into the array ",x);
		scanf("%i",&array[x]);
	}
	printf("\n");
	for(x=1; x<i; x++){
		printf("%i, ",array[x]);
	}
	printf("%i ",array[10]);
	for (x=0; x<i; x++){
		sum = sum + array[x+1];
	}
	printf("\n\nThe sum of the integers in the array is %i",sum);
	int_avg = sum/10.0;
	float_avg = (float)sum/(float)10.0;
	printf("\nThe integer average of the integers in the array is %i ",int_avg);
	printf("\nThe float average of the interers in the array is %.4f ", float_avg);
	printf("\n\n");
	bubble_sort(array,i);
	print(array,i);

	return 0;
}

