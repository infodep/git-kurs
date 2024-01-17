# Git Cheatsheet

Her finner du et par av de mest vanlige git-kommandoene.
Tekst inne i klammeparenteser (`[]`) skal erstattes, inkludert klammene

## Oversikt
-  [`git init`](#git-init)
-  [`git clone [url til et repo]`](#git-clone-[url-til-et-repo])
-  [`git add [filnavn]`](#git-add-[filnavn])
-  [`git add .`](#git-add-.)
-  [`git commit -m "[din commit-melding]"`](#git-commit--m-"[din-commit-melding]")
-  [`git push`](#git-push)
-  [`git remote add [url til en remote, f.eks et repo på github]`](#git-remote-add-[url-til-en-remote,-f.eks-et-repo-på-github])


### `git init`
Kjør denne i en mappe for å gjøre mappa til et repo

### `git clone [url til et repo]`
Lager en ny mappe for et repo på f.eks. github, og laster det ned

### `git add [filnavn]`
Legger til (stager) en fil for å kunne committes

### `git add .`
Stager alle filer med endringer

### `git commit -m "[din commit-melding]"`
Committer alle endringer som er staget med `git add`

### `git push`
Push de nye committene du har laget til serveren 

### `git remote add [url til en remote, f.eks et repo på github]`
Legg til en ny remote for å pushe til 
