# namefriend-camo

![Man in camoflauge fatigues and facepaint](./camo.jpg)

Generate usernames that blend in on namefriendy sites like HN, Reddit
using a neural network

## Installation

```
pipenv install
```

or Docker

```
docker build -t namefriend-camo .
docker run -it --rm namefriend-camo
```

## Usage

1. Scrape list of usernames:

    ```
    pipenv run scrapy crawl reddit
    ```

    or

    ```
    pipenv run scrapy crawl hacker_news
    ```

2.  Train neural network and generate names:

    Open a Python prompt

    ```
    pipenv run python3
    ```

    Train the neural network from the scraped usernames (more epochs = better):

    ```
    >>> from textgenrnn import textgenrnn
    >>> textgen = textgenrnn()
    >>> textgen.train_from_file('usernames/reddit.txt', num_epochs=10, new_model=True)
    ```

    Generate some usernames:

    ```
    >>> textgen.generate(3, temperature=1.0)
    thewaliboo
    buxthary1200
    4lifeffiex
    >>> textgen.generate(3, temperature=0.5)
    basticherdank
    botrenesson
    Dortinter
    >>> textgen.generate(3, temperature=0.2)
    Saringer
    Therestor
    surnangernan
    ```

    (Optional) Save the model for later use

    ```
    >>> textgen.save()
    ```
