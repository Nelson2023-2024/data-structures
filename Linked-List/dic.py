head = {
    "value": 11,
    "next":{
        "value": 23,
        "next":{
            "value":99,
            "next":{
                "value":12,
                "next":{
                    "value":34,
                    "next": None
                }
            }
        }
    }
}

print(head["next"]["next"]["value"])

#incase its a linked list
#  print(mylinked_list.next.next.value)