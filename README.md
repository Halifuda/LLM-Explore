# LLM-Explore  
Project of NLP in PKU  

.  
├── categories.py       # you can ignore it   
├── evaluate-logits.py  # 2.2.2 caculate percent of over-refuse and refuse  
├── evaluate.py         # 2.2.1 caculate percent of over-refuse and refuse  
├── explore.py          # 2.1, directly test on MMLU    
├── refuse-logits.py    # 2.2.2, let LLM say "I don't know"  
└── refuse.py           # 2.2.1, let LLM say "I don't know"     

## data  
[Data](https://people.eecs.berkeley.edu/~hendrycks/data.tar)  

## 2.2.1  
```bash  
python refuse.py -m <model-path>  
  
- `--ntrain`, `-k`: Number of training examples to use. Default is `5`.  
- `--data_dir`, `-d`: Directory containing the data. Default is `"data"`.  
- `--save_dir`, `-s`: Directory to save the results. Default is `"refuse-results"`.  
- `--model`, `-m`: Path to the model. Default is `"model\hub\LLM-Research\Llama-3___2-1B"`.  

```


