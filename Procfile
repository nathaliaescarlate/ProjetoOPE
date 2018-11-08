web: gunicorn Projeto_LMS.wsgi
log.Fatal(http.ListenAndServe(":" + os.Getenv("PORT"), router))