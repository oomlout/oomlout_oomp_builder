import action_all_default

def main(**kwargs):
    action_all_default.main(**kwargs)


if __name__ == "__main__":
    kwargs = {}
    
    filter = ""
    #filter = "spacer"
    #filter = "hardware"    
    #filter = "screw_socket_cap"
    #filter = "hardware_spacer_m3_id_7_mm_od_nylon_white_25_mm_length"
    
    kwargs["filter"] = filter
    main(**kwargs)
    