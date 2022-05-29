# # # import alpaca_trade_api.rest
# import pydoc

# f = open("demofile2.txt", "a")
# f.write(pydoc.render_doc(help(alpaca_trade_api.rest)))
# f.close()

# simplified version of sending help() output to a file
import sys
# save present stdout
out = sys.stdout
fname = "help_print7.txt"
# set stdout to file handle
sys.stdout = open(fname, "w")
# run your help code
# its console output goes to the file now
help('alpaca_trade_api.rest')
sys.stdout.close()
# reset stdout
sys.stdout = out