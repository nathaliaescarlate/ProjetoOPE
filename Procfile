web: gunicorn Projeto_LMS.wsgi --log-file
log.Fatal(http.ListenAndServe(":" + os.Getenv("PORT"), router))