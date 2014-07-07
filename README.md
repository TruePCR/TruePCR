qPRC
====
Web UI for visualising DNA concentration over time.

Notebook
--------
While developing the workflow, we are using a Python notebook.
Assuming you have your
[Python sci dev environment set up](http://www.scipy.org/install.html),
you can start it with:

    cd notebook
    ipython notebook --pylab=inline

And see it in your browser at [http://127.0.0.1:8888/](http://127.0.0.1:8888/).

If you just want to view the contents, you can see it on
[nbviewer][notebook-nbviewer] without installing anything.

[notebook-nbviewer]: http://nbviewer.ipython.org/urls/raw.githubusercontent.com/qPRC/qPRC/master/notebook/qPRC.ipynb "qPRC workflow notebook"

Web app
-------

### Development

Get ready:

    mkvirtualenv -p /usr/bin/python3 qPRC
    pip install -r requirements/dev.txt
    npm install
    bower install
    grunt build

See if any migrations are necessary:

    ./manage.py migrate

Link up your front+backend:

    util/bootstrap.sh

Then in one tab spin up the frontend workflow:

    grunt serve

And in another the backend workflow:

    ./manage.py runserver_plus


### Production

Everything the same, except:

    pip install -r requirements/prod.txt
    util/boostrap.sh prod

Or use the prod brunch:

    grunt publish
    cd prod
    git checkout prod
    ./manage.py runserver
