num = int(input())

if num < 1:
    print('no army')
elif num < 10:
    print('few')
elif num < 50:
    print('pack')
elif num < 500:
    print('horde')
elif num < 1000:
    print('swarm')
else:
    print('legion')
