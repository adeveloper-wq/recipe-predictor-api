# Recipe predictor (German, GPT-2, Transformers)
- fine tuned [dbmdz/german-gpt2](https://huggingface.co/dbmdz/german-gpt2) with ~100000 recipes from Chefkoch (primarly cake and dessert type stuff)
- followed [this tutorial](https://towardsdatascience.com/fine-tune-a-non-english-gpt-2-model-with-huggingface-9acc2dc7635b) and used [this](https://github.com/adeveloper-wq/Chefkoch-API) for the crawling of the recipes
- given a german start of a sentence the model generates following text

## How to run
- `docker-compose up`
- accessible on port 8000 and on the route `/{start_of_a_sentence}`
