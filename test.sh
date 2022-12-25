#!/bin/sh
HOST=0.0.0.0 PORT=5000 N=3 python services/fizz & HOST=0.0.0.0 PORT=5001 M=5 python services/buzz & HOST=0.0.0.0 PORT=5002 python services/concat & HOST=0.0.0.0 PORT=5003 FIZZ_HOST=http://127.0.0.1:5000 BUZZ_HOST=http://127.0.0.1:5001 CONCAT_HOST=http://127.0.0.1:5002 python services/main
