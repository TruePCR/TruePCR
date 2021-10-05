TruePCR [![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.45660.svg)](http://dx.doi.org/10.5281/zenodo.45660)
====
Jupyter notebook and web UI for modelling visualising DNA concentration over time.

Notebook
--------
While developing the workflow, we are using a Jupyter notebook.
Assuming you have your
[Python sci dev environment set up](http://www.scipy.org/install.html)
(Python 3.5 was used during development),
you can start it from the root of the git repository with:

    jupyter notebook --notebook-dir=./notebook

And see it in your browser at <http://127.0.0.1:8888/>.

If you just want to view the contents, you can see it on
[nbviewer][notebook-nbviewer] without installing anything.

[notebook-nbviewer]: https://nbviewer.jupyter.org/github/TruePCR/TruePCR/blob/master/notebook/TruePCR.ipynb "TruePCR workflow notebook"

Web app
-------

### Development

Assuming a Python sci/dev environment, which would on e.g. OS X be more or less:

 - install OS X command line tools (or Xcode)
 - install [Homebrew](http://brew.sh/)
 - install some binary dependencies

        brew install python3 gcc freetype

 - install some Python global dependencies

        pip install virtualenvwrapper

Get ready:

    mkvirtualenv -p /usr/bin/python3 TruePCR
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

## Deployment

To deploy to Heroku, from the repo root run:

    grunt publish
    (cd prod; git push heroku prod:master)
