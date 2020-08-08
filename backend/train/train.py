import gpt_2_simple as gpt2

##################
# Hyperparameters
num_steps = 20000
print_steps = 10
sample_steps = 500
save_steps = 500
##################

sess = gpt2.start_tf_sess()

gpt2.finetune(sess,
              dataset="output/text_encoded.npz",
              steps=num_steps,
              restore_from='fresh',
              print_every=print_steps,
              sample_every=sample_steps,
              save_every=save_steps,
              model_name='124M',
              batch_size=1,
              sample_length=256
              )