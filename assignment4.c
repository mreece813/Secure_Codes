/* Michael Reece
 * 177000762
 * 10/12/2019 */

#include <gtk/gtk.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>

static void callback (GtkWidget *widget, gpointer data);
static gboolean delete_event (GtkWidget *widget, GdkEvent *event, gpointer data);

int main (int argc, char *argv[])
{
  char *name[3] = {"assignment1","assignment2","assignment3"};	/* assignments called in the Makefile */
  char title[50];
  char *label[3]={"Shell Script","Fence Panels","Integer Arrays"}; /* labels in the window */
  int i;
  GtkWidget *window;
  GtkWidget *button[3];
  GtkWidget *box1;

  gtk_init (&argc,&argv);
  window = gtk_window_new (GTK_WINDOW_TOPLEVEL);
  gtk_window_set_title (GTK_WINDOW (window), "My Assignments");	/* Makes the header of the window */
  gtk_window_set_position (GTK_WINDOW (window), GTK_WIN_POS_CENTER);
  g_signal_connect (window, "delete-event", G_CALLBACK (delete_event), NULL);
  gtk_container_set_border_width (GTK_CONTAINER (window), 60);

  box1 = gtk_vbox_new (FALSE, 0);
  gtk_container_add (GTK_CONTAINER (window), box1);

  for (i = 0; i < 3; i++)	/* Making the buttons for the window */
  {
    strcpy(title,"Run  ");	/* puts Run before all the labels */
    button[i] = gtk_button_new_with_label (strcat(title,label[i])); /* Uses the labels made for the window */
    g_signal_connect (button[i], "clicked", G_CALLBACK (callback), name[i]); /* Grabs the actual assignment number */
    gtk_box_pack_start (GTK_BOX (box1), button[i], TRUE, TRUE, 0);
    gtk_widget_show (button[i]);
  }

  gtk_widget_show (box1);
  gtk_widget_show (window);

  gtk_main();
  return 0;
}

static void callback (GtkWidget *widget, gpointer data)
	/* Runs the files that was chosen in the window */
{
  char run[50];
  strcpy(run, "./");
  g_print ("You have chosen to run %s\n", strcat(run, (gchar *) data));
  system(run);
}

static gboolean delete_event (GtkWidget *widget, GdkEvent *event, gpointer data)
	/* deletes the window that is running */
{
  gtk_main_quit ();
  return FALSE;
}
