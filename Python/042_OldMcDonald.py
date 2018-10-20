sound = {"cow": "moo", "chicken": "cluck"}

for k, v in sound.items():
    print("old mcdonald had a farm. And on that farm he had a {}".format(k))
    print("with a {} {} here and a {} there.".format(sound[k], sound[k], sound[k]))

# ANSWER by magwhich
animals= ['cow','chicken','turkey','kangaroo','t-rex','road runner']
sounds=['moo','cluck','gobble',"G'day",'raagh','meep-meep']
for x in range(len(animals)):
    print("old mc donald had a farm e-i e-i o")
    print("and on this farm he had an",animals[x])
    print("e-i e-i o")
    print("with a ",sounds[x], "and a" ,sounds[x], "there")
    print("old mc donald had a farm e-i e-i o")
print("old mc donald made strange investmets in livestock e-i-e-i-o")

# SUMMARY
# The magwhich answer is a good example of why to use a dictionary instead of a list
# First of all it does not matter when each animal appears, in fact, it's intendd
# to be a little random. Secondly, if a person wants to make a change to something in
# therer list then it will require counting out where the item should be added or alterd
# Finally, the animals and sounds lists are intinsically linked so housekeeping on this list
# will be more effort than keeping a single dictionary.
# If the user wanted to keep it to lists though then a list within a list would be fine e.g.
animals_and_sounds = [['cow', 'moo'],
                      ['chicken', 'cluck'],
                      ['T-rex','raagh']]

