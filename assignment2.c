#include<stdio.h>
// Michael Reece
// 177000762
// 3/10/2019
// Stackoverflow and notes in class were used

int main()
{
	int fence_need,small_panel, large_panel,sm_lg,special,small_qty,large_qty;
	printf("Measurement of the fencing needed (feet): ");
	scanf("%i",&fence_need);
	while(fence_need < 1)//This will repeat until user inputs a number larger than 0
	{
		printf("Please enter an integer > 0: ");
		scanf("%i",&fence_need);
	}
	printf("Enter the size of smaller panel in feet: ");
	scanf("%i",&small_panel);
	while(small_panel < 1)//This will repeat until the user inputs a number larger than 0
	{
		printf("Please enter an integer > 0:  ");
		scanf("%i",&small_panel);
	}
	large_panel = small_panel + 2;// This will create the larger panal
	printf("The larger panel will be %i feet.\n",large_panel); //This outputs the larger panal number
	printf("Happy Building!!\n");
	sm_lg = small_panel + large_panel; //This variable is made to help find the qty later
	special = fence_need % sm_lg; //This is for getting the special order
	small_qty = fence_need / sm_lg; //This gets you the small qty
	large_qty = fence_need / sm_lg; //This gets you the large qty
	if (special > large_panel)//This will increase the larger_qty by one
	{
		large_qty = large_qty + 1;
		special = special - large_panel;
	}
	else if(special == large_panel)
	{
		large_qty = large_qty + 1;
		special = 0;
	}
	else if(special % small_panel == 0)//This will increase the small qty by one
	{
		small_qty = (special / small_panel) + small_qty;
		special = 0;
	}
	else if (special > small_panel)	
	{
		small_qty = small_qty + 1;
		special = special - small_panel;
	}
	printf("The fence will need %i  qty %i foot panel(s) and %i qty %i foot panel(s).",small_qty,small_panel,large_qty,large_panel);
	printf("\n");
	if (special != 0)//This will print out the special order if there is any left
	{
		printf("Plus a special order %d foot panel.",special);
		printf("\n");
	}

	return 0;

}
