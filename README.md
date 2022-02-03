This web service allows you to find out the possible moves for the selected chess piece on the selected field on the chessboard. To run the project, just run the main.py file. To work with the service, send requests to the server in the form "api/v1/{figure_name}/{current_field}", to display all possible fields for the move of this figure from the entered field and "api/v1/{figure_name}/{current_field}/{dest_field}", to display an answer, is it possible to move this figure from the current_field field to the dest_field field. The response is sent in json format.
