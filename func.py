def solve_hanoi_tower_problem(num_disks:int, source:str, destination:str, auxiliary:str):
    if num_disks == 1:
        print(f"disk 1 from {source} to ------> to {destination}.")
        return 0
    
    solve_hanoi_tower_problem(num_disks=num_disks-1, source=source, destination=auxiliary, auxiliary=destination)
    print(f"disk {num_disks} from {source} to ------> to {destination}.")
    solve_hanoi_tower_problem(num_disks=num_disks-1, source=auxiliary, destination=destination, auxiliary=source)
    
    
    