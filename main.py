from maps.k25029 import k25029susume
from maps.k25061 import k25061
from maps.K25043Osusume import K25043Sample
from maps.K25078Osusume import K25078Osusume

# ↓のリストには、メンバーの各オススメ学食が格納されます。
data = [k25029susume(), 
        k25061(),
        K25043Sample(),
        K25078Osusume()
        ]

for rank, d in enumerate(data, start=1):
    print(f"{rank}位: {d.get_menu()}")
    print("---------------------------------")
    print(d.get_summary())
    print(d.get_author())