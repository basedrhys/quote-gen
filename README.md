# AI-Powered Quote Generator
Novel quote generator using GPT-2. The app is currently hosted [here](https://gpt2-quote.appspot.com/), feel free to play around!.

This project was based off minimaxir's [gpt-2-cloud-run](https://github.com/minimaxir/gpt-2-cloud-run) project.

## Frontend

The web interface is based off the UI in minimaxir's repo. It's hosted using Google App Engine which works great for small project-showoff apps with its automatic scaling (down to 0).

## Backend

The API is hosted using Google Cloud Run, Google's Docker container serving service. It's probably one of the easiest ways to easily deploy custom ML models for inference, and again has automatic scaling down to 0 instances (for the cost-mindful like myself).

## Train Your Own

The dataset was sourced from the [500k Quote Dataset](https://github.com/ShivaliGoel/Quotes-500K), with a little pre-processing to get it into the right format.

[Quote Dataset](https://drive.google.com/file/d/18fUCkPeVkC3MiOji5K8rzU9jXvZfC1Im/view?usp=sharing)

[Colab Notebook](https://colab.research.google.com/drive/1dy1lj6uFmgvsiaHxjNwy3A1wI9W0PmwW)

Also, look at minimaxir's [Colab notebook](https://colab.research.google.com/drive/1VLG8e7YSEwypxU-noRNhsv5dW4NfTGce) for more instruction in using the library.

## Quote Samples

- **Life**: When you have the ability to have a life, you should have the choice to live it. - Roy T. Bennett
- **Love**: I'm sorry, but I can't be serious anymore. I can't give you your heart, and I'd rather give you my heart. - James Patterson
- **Inspirational**: I have never held in my hands any that I did not know. - Paulo Coelho
- **Inspirational**: The best way to survive a long, long time is to only see what happens to you. - Steve Maraboli

As you can see, generating quotes is a *little* difficult for the GPT2 model, at least with this dataset. Many of them sound quite good (and dare I say it **deep**). However, the limitations of current transformer-based language models become very apparent in this instance: the model can generate quotes with perfect syntax that sound like perfect english, however, they often are non-sensical or contradicting. The value in quotes is often derived from their word-play and clever use of the english language, which the model doesn't have a firm knowledge of. Despite this, it's still an interesting experiment, and raises some deeper questions about what makes quotes actually *deep* or *resounding* with us, and whether these can be feigned by AI.

