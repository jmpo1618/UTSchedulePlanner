from Planner import Planner


if __name__ == "__main__":
    print 'Insert EID:'
    eid = raw_input()
    print 'Insert Password:'
    pwd = raw_input()
    p = Planner(eid, pwd)
    while True:
        print "Enter command:"
        cmd = raw_input()
        if cmd == "add":
            print "Enter unique number to add:"
            unique_number = raw_input()
            p.add_class(unique_number)
