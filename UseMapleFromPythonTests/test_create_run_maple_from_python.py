import os
import sys
sys.path.append('./')

id = "oyl"
timeout = 10
initial_directory = os.path.join(os.path.dirname(__file__),'..','..')
auxiliar_file = os.path.join(initial_directory, '03CADVariableOrdering',
                             "Auxiliar", "maple_from_python_file_proj"
                             + id + ".mpl")
output_file = os.path.join(initial_directory, '03CADVariableOrdering',
                           "Auxiliar", "maple_from_python_output"+id+".txt")


def test_create_run_maple_from_python_gcd():
    """This is a shitty test but it is best than anything."""
    from UseMapleFromPython import create_run_maple_from_python
    aux = create_run_maple_from_python(
        file_location=auxiliar_file,  # equvalent to
        initializations=[("a", 6), ("b", -8)],  # a:=6:b=-8:
        functions_to_call=[("gcd",
                           ["a", "b"],
                           "result")],  # result := gcd(a,b)
        output_files=[(output_file, "result")], timelimit=timeout) # (python) aux[2] = result 

    assert aux[2] == 2, ("The return number is not the gcd")


def test_create_run_maple_from_python_projection():
    """This is a shitty test but it is best than anything."""
    from UseMapleFromPython import create_run_maple_from_python
    polynomials = [[[1, 0, 1]], [[0, 1, 1]], [[0, 0, -213], [0, 1, 655]]]
    variable = 1
    aux = create_run_maple_from_python(
        file_location=auxiliar_file,
        libnames_needed=[os.path.join(initial_directory,
                                      "02Tools", "MapleTools")],
        packages_needed=["TeresoTools"],
        initializations=[("polynomials_python", polynomials)],
        functions_to_call=[("projection_step_from_python",
                           ["polynomials_python", str(variable)],
                           "proj_polys")],
        output_files=[(output_file, "proj_polys")], timelimit=timeout)

    assert aux[2] == [[[1, 1]], [[0, -213], [1, 655]]], ("The return"
           "polynomials aren't the projection")


test_create_run_maple_from_python_gcd()