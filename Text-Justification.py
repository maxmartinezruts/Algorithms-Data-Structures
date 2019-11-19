"""
Author: Max Martinez Ruts
Date: October 2019
Description:

Dynamic programming approach to optimally split a text into a set of lines by minimizing the added cost of all lines
 where the cost of a line is minimum if the lenght of the line equals the desired target lenght  t (AKA text justification)

Complexity: O(n^2)
Proof:
Dynamic approach using memoization, where time complexity = # Guesses * O(guess) = n^2 * O(1) = O(n^2)
"""

import math

memo = {}

def J(words):

    line = ' '.join(words)

    if line in memo:
        return memo[line]

    print(line)

    if len(line)<40:
        memo[line] = [line]
        return [line]

    min_split_cost = math.inf
    min_split = None

    for i in range(1,len(words)):
        cost_split = cost_lines([words[:i]]) + cost_lines(J(words[i:]))

        if cost_split < min_split_cost:
            min_split_cost = cost_split
            min_split = i


    solution = [words[:min_split]] +J(words[min_split:])
    memo[line] = solution

    return solution

# Calculate added cost of all lines
def cost_lines(lines):
    cost = 0
    for line in lines:
        text = ' '.join(line)
        cost += (40-len(text))**2
    return cost

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Tellus in metus vulputate eu scelerisque. Pellentesque id nibh tortor id aliquet. Neque viverra justo nec ultrices dui sapien eget. Amet consectetur adipiscing elit ut aliquam purus sit amet. Orci phasellus egestas tellus rutrum tellus. Elementum pulvinar etiam non quam lacus. Amet consectetur adipiscing elit pellentesque habitant. Libero enim sed faucibus turpis. Justo nec ultrices dui sapien eget mi proin. Odio morbi quis commodo odio aenean. Turpis egestas sed tempus urna et pharetra pharetra massa. Blandit aliquam etiam erat velit. Senectus et netus et malesuada fames ac turpis egestas. Auctor urna nunc id cursus metus. Auctor elit sed vulputate mi sit amet mauris commodo. Eget arcu dictum varius duis at consectetur lorem donec massa. Enim sed faucibus turpis in eu mi bibendum." \
       "Laoreet id donec ultrices tincidunt arcu non. Augue neque gravida in fermentum et sollicitudin ac orci. Tortor vitae purus faucibus ornare suspendisse sed nisi. A diam sollicitudin tempor id eu nisl nunc mi. Enim ut sem viverra aliquet eget sit amet tellus cras. Suspendisse sed nisi lacus sed. Viverra ipsum nunc aliquet bibendum enim. Ut etiam sit amet nisl purus. Ut consequat semper viverra nam libero. Malesuada fames ac turpis egestas integer eget aliquet nibh praesent. Accumsan tortor posuere ac ut consequat semper viverra. Risus feugiat in ante metus dictum. Sagittis eu volutpat odio facilisis mauris. Pharetra convallis posuere morbi leo urna molestie at elementum. Feugiat sed lectus vestibulum mattis ullamcorper velit sed ullamcorper. Elit at imperdiet dui accumsan sit amet. Lacus viverra vitae congue eu. Facilisis volutpat est velit egestas dui id ornare arcu odio. Nam libero justo laoreet sit amet cursus sit amet dictum. Eu turpis egestas pretium aenean pharetra magna." \
       "Non pulvinar neque laoreet suspendisse interdum consectetur. Diam vel quam elementum pulvinar etiam non quam lacus. Congue mauris rhoncus aenean vel. Integer feugiat scelerisque varius morbi enim nunc faucibus. Ultrices in iaculis nunc sed. Dis parturient montes nascetur ridiculus mus mauris. Ut consequat semper viverra nam libero. Blandit libero volutpat sed cras ornare arcu dui vivamus. Ridiculus mus mauris vitae ultricies leo integer malesuada nunc vel. Semper eget duis at tellus at urna condimentum. Rhoncus est pellentesque elit ullamcorper dignissim cras tincidunt lobortis. Nibh cras pulvinar mattis nunc sed blandit libero volutpat sed. Enim lobortis scelerisque fermentum dui faucibus in. Feugiat sed lectus vestibulum mattis ullamcorper velit sed ullamcorper. Amet nisl suscipit adipiscing bibendum. Nunc faucibus a pellentesque sit. Tellus at urna condimentum mattis pellentesque." \
       "Dignissim diam quis enim lobortis scelerisque fermentum dui. Aliquet sagittis id consectetur purus ut faucibus pulvinar. Suspendisse faucibus interdum posuere lorem ipsum dolor sit amet consectetur. Condimentum vitae sapien pellentesque habitant morbi tristique. Donec et odio pellentesque diam volutpat. Odio pellentesque diam volutpat commodo sed egestas egestas fringilla phasellus. Diam quis enim lobortis scelerisque. Curabitur vitae nunc sed velit dignissim sodales ut. Fames ac turpis egestas integer. Cursus metus aliquam eleifend mi in. Nisl pretium fusce id velit. Risus commodo viverra maecenas accumsan lacus. Ac tortor dignissim convallis aenean et tortor at. Ut tellus elementum sagittis vitae et leo duis ut. Massa tempor nec feugiat nisl pretium fusce. Pellentesque nec nam aliquam sem. Sapien eget mi proin sed libero enim sed faucibus turpis. Sit amet porttitor eget dolor morbi non arcu risus. Lacus suspendisse faucibus interdum posuere lorem ipsum. Mi in nulla posuere sollicitudin aliquam.Enim diam vulputate ut pharetra sit amet aliquam id diam. Ullamcorper eget nulla facilisi etiam dignissim. Enim nulla aliquet porttitor lacus luctus accumsan tortor posuere ac. Vitae auctor eu augue ut lectus arcu. Purus semper eget duis at tellus at urna condimentum. Sit amet luctus venenatis lectus magna fringilla urna. Nisl purus in mollis nunc sed id. Tristique risus nec feugiat in fermentum. Aliquet nibh praesent tristique magna sit amet purus. Nunc consequat interdum varius sit amet mattis vulputate enim nulla. Pulvinar elementum integer enim neque." \
       "Egestas sed sed risus pretium quam vulputate dignissim suspendisse in. Dolor sed viverra ipsum nunc aliquet. Quis blandit turpis cursus in hac habitasse. Vehicula ipsum a arcu cursus vitae congue mauris rhoncus aenean. Suspendisse ultrices gravida dictum fusce. Vitae purus faucibus ornare suspendisse sed nisi lacus. Habitant morbi tristique senectus et netus et malesuada fames. Sem integer vitae justo eget. Morbi leo urna molestie at elementum eu. Non diam phasellus vestibulum lorem sed. Leo a diam sollicitudin tempor id eu nisl nunc. Urna neque viverra justo nec ultrices dui sapien eget. Volutpat maecenas volutpat blandit aliquam etiam erat velit. Tortor consequat id porta nibh venenatis cras."

lines = [text]

words = text.split(' ')

lines = J(words)
print('finished')
for line in lines:
    print(' '.join  (line) )

