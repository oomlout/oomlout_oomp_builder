import action_load
import action_create
import action_make_links

utilities = []
utilities.append("oomlout_oomp_utility_readme_generation")

def main(**kwargs):
    #action_create.main(**kwargs)
    #action_load.main(**kwargs)    
    #action_make_links.main(**kwargs)

    #for utility in utilities:
    #    utility_module = __import__(f"temporary/{utility}/working")
    #    utility_module.main(**kwargs)

    import temporary.oomlout_oomp_utility_readme_generation.working
    temporary.oomlout_oomp_utility_readme_generation.working.main(**kwargs)





if __name__ == "__main__":
    kwargs = {}
    main(**kwargs)