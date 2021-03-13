# Diary

## Coding involves a lot of research, trial and error. Here's a log of development issues.

### Fixed issues

#### ingredients/new.html sends 'GET' instead of 'POST'

If form method is written as 'methods' the form will always use GET to submit.

#### CamelCase and Postgre-SQL

Apparently in Postgres database table row names, as well as method names, are case-insensitive. To avoid reconfigurations, one should try to name table rows using underscores instead. 

#### How to filter a relationship as a query

In order to work with a table relationship through queries, one needs to configure it with lazy='dynamic'.

### Unfixed issues

#### First item on ingredient lists (both list and listall) can not be deleted

The recipe specific ingredient listing is deletionwise unresponsive, but interestingly only for the first element of the list.
On the list all ingredients page the first list element sends to a 504 error page.

This boiled down to the same error: if the listing method on views.py for the ingredients accepts both GET and POST,
the delete call is unresponsive (but still only for the first element of the list!), and if POST is left out, then the response is a 504 error page. 

Because the errors are both this similar, it is reasonable to assume they originate from the same source, or at least a repeated mistake on the code.
This problem does not apply to the recipes. 

