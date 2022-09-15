# url shortener

### download

```bash
git clone
```

### run

```bash
docker-compose build && docker-compose up
```

### access
```bash
http://0.0.0.0:5000/
```

--------------

notes: 
the implementation is super trivial and straightforward using the 3rd party libs & tools, there was no specification on how it should be done so the easiest way is the way to go. In case there was a need for more production-like state it should have been specified in details, namely:
- how long the short url should be
- what is the expected traffic to such a service
- how many urls will be stored in db
- how long will the urls stay in db
- etc.

based on that the url-shortening algorithm could be implemented
