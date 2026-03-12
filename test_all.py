### NO MODIFICAR ESTE ARCHIVO.
# FREEZE CODE BEGIN
import subprocess
import sys


def run_program(filename, inputs):
    """Ejecuta un programa Python con una lista de inputs simulados."""
    process = subprocess.Popen(
        [sys.executable, filename],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    input_text = "\n".join(inputs)
    stdout, stderr = process.communicate(input=input_text)
    return stdout


def import_from(filename, name):
    """Importa un atributo (función/variable) desde un archivo .py dado su path."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("mod", filename)
    mod = importlib.util.load_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, name)


# ============ TESTS PARA functions.py (P1) ============
class TestFunctions:
    def setup_method(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location("functions", "functions.py")
        self.mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.mod)

    def test_basic_average(self):
        result = self.mod.promedio_estudiante([85, 92, 78])
        assert result == 85.0

    def test_returns_float(self):
        result = self.mod.promedio_estudiante([10, 20, 30])
        assert isinstance(result, float)

    def test_whole_number_is_float(self):
        result = self.mod.promedio_estudiante([100, 100])
        assert result == 100.0
        assert isinstance(result, float)

    def test_single_element(self):
        result = self.mod.promedio_estudiante([50])
        assert result == 50.0

    def test_empty_list(self):
        result = self.mod.promedio_estudiante([])
        assert isinstance(result, float)

    def test_decimal_average(self):
        result = self.mod.promedio_estudiante([1, 2])
        assert result == 1.5

    def test_all_zeros(self):
        result = self.mod.promedio_estudiante([0, 0, 0])
        assert result == 0.0

    def test_large_list(self):
        result = self.mod.promedio_estudiante([10, 20, 30, 40, 50])
        assert result == 30.0


# ============ TESTS PARA return_types.py (P2) ============
class TestReturnTypes:
    def setup_method(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location("return_types", "return_types.py")
        self.mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.mod)

    def test_integer_input_returns_float(self):
        import unittest.mock as mock
        with mock.patch("builtins.input", return_value="25") as mock_input:
            self.mod.obtener_precio_usuario()
        mock_input.assert_called_once()
        call_arg = mock_input.call_args[0][0] if mock_input.call_args[0] else ""
        assert "price" in call_arg.lower() or "precio" in call_arg.lower()

    def test_returns_float_type(self):
        import unittest.mock as mock
        with mock.patch("builtins.input", return_value="25"):
            result = self.mod.obtener_precio_usuario()
        assert isinstance(result, float)

    def test_integer_becomes_float(self):
        import unittest.mock as mock
        with mock.patch("builtins.input", return_value="25"):
            result = self.mod.obtener_precio_usuario()
        assert result == 25.0

    def test_float_input(self):
        import unittest.mock as mock
        with mock.patch("builtins.input", return_value="9.99"):
            result = self.mod.obtener_precio_usuario()
        assert result == 9.99

    def test_zero_input(self):
        import unittest.mock as mock
        with mock.patch("builtins.input", return_value="0"):
            result = self.mod.obtener_precio_usuario()
        assert result == 0.0

    def test_large_value(self):
        import unittest.mock as mock
        with mock.patch("builtins.input", return_value="1000"):
            result = self.mod.obtener_precio_usuario()
        assert result == 1000.0


# ============ TESTS PARA function_types.py (P3) ============
class TestFunctionTypes:
    def setup_method(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location("function_types", "function_types.py")
        self.mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.mod)

    def test_calc_avg_basic(self):
        assert self.mod.calc_avg([2.0, 4.0, 6.0, 8.0]) == 5.0

    def test_calc_avg_single(self):
        assert self.mod.calc_avg([10.0]) == 10.0

    def test_list_shift_modifies_in_place(self):
        data = [2.0, 4.0, 6.0, 8.0]
        self.mod.list_shift(data, -5.0)
        assert data == [-3.0, -1.0, 1.0, 3.0]

    def test_list_shift_positive(self):
        data = [1.0, 2.0, 3.0]
        self.mod.list_shift(data, 10.0)
        assert data == [11.0, 12.0, 13.0]

    def test_list_shift_returns_none(self):
        data = [1.0, 2.0]
        result = self.mod.list_shift(data, 1.0)
        assert result is None

    def test_print_normalized_returns_none(self):
        result = self.mod.print_normalized([1.0, 2.0])
        assert result is None

    def test_full_normalization_workflow(self):
        data = [2.0, 4.0, 6.0, 8.0]
        avg = self.mod.calc_avg(data)
        self.mod.list_shift(data, -avg)
        assert data == [-3.0, -1.0, 1.0, 3.0]


# ============ TESTS PARA scope.py (P4) ============
class TestScope:
    def setup_method(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location("scope", "scope.py")
        self.mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.mod)

    def test_defaults_are_none(self):
        assert self.mod.get_globals() == (None, None)

    def test_set_and_get(self):
        self.mod.set_globals(10, "Hello")
        assert self.mod.get_globals() == (10, "Hello")

    def test_returns_tuple(self):
        result = self.mod.get_globals()
        assert isinstance(result, tuple)

    def test_update_globals(self):
        self.mod.set_globals(1, "first")
        self.mod.set_globals(99, "second")
        assert self.mod.get_globals() == (99, "second")

    def test_set_globals_returns_none(self):
        result = self.mod.set_globals(5, "test")
        assert result is None

    def test_int_and_str_types(self):
        self.mod.set_globals(42, "world")
        val_int, val_str = self.mod.get_globals()
        assert isinstance(val_int, int)
        assert isinstance(val_str, str)


# ============ TESTS PARA modules.py (P5) ============
class TestModules:
    def test_cwd_in_output(self):
        output = run_program("modules.py", ["10"])
        assert "Current working directory:" in output

    def test_log_output_10(self):
        output = run_program("modules.py", ["10"])
        assert "Log base 2 of 10 is: 3.321928094887362" in output

    def test_floor_10(self):
        output = run_program("modules.py", ["10"])
        assert "Floor: 3" in output

    def test_ceiling_10(self):
        output = run_program("modules.py", ["10"])
        assert "Ceiling: 4" in output

    def test_log_output_16(self):
        output = run_program("modules.py", ["16"])
        assert "Log base 2 of 16 is: 4.0" in output

    def test_floor_ceiling_equal_16(self):
        output = run_program("modules.py", ["16"])
        assert "Floor: 4" in output
        assert "Ceiling: 4" in output

    def test_prompt_present(self):
        output = run_program("modules.py", ["8"])
        assert "Enter an integer:" in output


# ============ TESTS PARA multiple_files.py (P6) ============
class TestMultipleFiles:
    def test_example_input(self):
        output = run_program("multiple_files.py", ["The sun sets behind the tall hills"])
        assert "Your encoded message is: sllih llat eht dniheb stes nus ehT1" in output

    def test_no_a_letters(self):
        output = run_program("multiple_files.py", ["hello world"])
        assert "Your encoded message is: dlrow olleh0" in output

    def test_multiple_a_letters(self):
        output = run_program("multiple_files.py", ["banana"])
        assert "Your encoded message is: ananab3" in output

    def test_prompt_present(self):
        output = run_program("multiple_files.py", ["test"])
        assert "Please type your message" in output

    def test_output_label_present(self):
        output = run_program("multiple_files.py", ["abc"])
        assert "Your encoded message is:" in output

    def test_single_word(self):
        output = run_program("multiple_files.py", ["cat"])
        assert "Your encoded message is: tac1" in output


# ============ TESTS PARA random_q.py (P7) ============
class TestRandomQ:
    def test_seed_123_range_10_20(self):
        output = run_program("random_q.py", ["10", "20"])
        assert "Generated random number: 10" in output

    def test_seed_123_range_1_100(self):
        output = run_program("random_q.py", ["1", "100"])
        assert "Generated random number: 7" in output

    def test_seed_123_range_50_60(self):
        output = run_program("random_q.py", ["50", "60"])
        assert "Generated random number: 50" in output

    def test_start_prompt_present(self):
        output = run_program("random_q.py", ["1", "10"])
        assert "Enter the start value:" in output

    def test_end_prompt_present(self):
        output = run_program("random_q.py", ["1", "10"])
        assert "Enter the end value:" in output

    def test_output_label_present(self):
        output = run_program("random_q.py", ["1", "10"])
        assert "Generated random number:" in output


# ============ TESTS PARA debugging.py (P8) ============
class TestDebugging:
    def test_sample_1_total(self):
        output = run_program("debugging.py", ["12000 8000 9500 11000 5000 13000 10000"])
        assert "Total steps: 68500" in output

    def test_sample_1_average(self):
        output = run_program("debugging.py", ["12000 8000 9500 11000 5000 13000 10000"])
        assert "Average daily steps: 9785" in output

    def test_sample_1_max(self):
        output = run_program("debugging.py", ["12000 8000 9500 11000 5000 13000 10000"])
        assert "Highest steps in a day: 13000" in output

    def test_sample_1_min(self):
        output = run_program("debugging.py", ["12000 8000 9500 11000 5000 13000 10000"])
        assert "Lowest steps in a day: 5000" in output

    def test_sample_1_goal(self):
        output = run_program("debugging.py", ["12000 8000 9500 11000 5000 13000 10000"])
        assert "Goal met each day: [True, False, False, True, False, True, True]" in output

    def test_sample_2_all_equal(self):
        output = run_program("debugging.py", ["10000 10000 10000 10000 10000 10000 10000"])
        assert "Total steps: 70000" in output
        assert "Average daily steps: 10000" in output
        assert "Goal met each day: [True, True, True, True, True, True, True]" in output

    def test_sample_3_with_zeros(self):
        output = run_program("debugging.py", ["0 5000 10000 0 12000 3000 8000"])
        assert "Total steps: 38000" in output
        assert "Average daily steps: 5428" in output
        assert "Lowest steps in a day: 0" in output
        assert "Goal met each day: [False, False, True, False, True, False, False]" in output

    def test_average_is_int(self):
        output = run_program("debugging.py", ["10000 10000 10000 10000 10000 10000 10000"])
        # Si fuera float aparecería como 10000.0
        assert "Average daily steps: 10000\n" in output

    def test_goal_contains_booleans_not_strings(self):
        output = run_program("debugging.py", ["10000 10000 10000 10000 10000 10000 10000"])
        assert "'True'" not in output
        assert "[True" in output


# ============ TESTS PARA debug.py (P11) ============
class TestDebug:
    def test_max_is_middle(self):
        output = run_program("debug.py", ["10", "25", "13"])
        assert "Maximum value: 25" in output

    def test_max_is_first(self):
        output = run_program("debug.py", ["99", "10", "50"])
        assert "Maximum value: 99" in output

    def test_max_is_last(self):
        output = run_program("debug.py", ["5", "3", "100"])
        assert "Maximum value: 100" in output

    def test_all_equal(self):
        output = run_program("debug.py", ["7", "7", "7"])
        assert "Maximum value: 7" in output

    def test_negative_numbers(self):
        output = run_program("debug.py", ["-1", "-5", "-3"])
        assert "Maximum value: -1" in output

    def test_prompt_present(self):
        output = run_program("debug.py", ["1", "2", "3"])
        assert "Enter a number:" in output

    def test_prompt_appears_three_times(self):
        output = run_program("debug.py", ["1", "2", "3"])
        assert output.count("Enter a number:") == 3


# ============ TESTS PARA celsius_to_fahrenheit.py (P12) ============
class TestCelsiusToFahrenheit:
    def setup_method(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location("celsius_to_fahrenheit", "celsius_to_fahrenheit.py")
        self.mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.mod)

    def test_freezing(self):
        assert self.mod.celsius_to_fahrenheit(0) == 32.0

    def test_boiling(self):
        assert self.mod.celsius_to_fahrenheit(100) == 212.0

    def test_negative_forty(self):
        assert self.mod.celsius_to_fahrenheit(-40) == -40.0

    def test_returns_float(self):
        result = self.mod.celsius_to_fahrenheit(0)
        assert isinstance(result, float)

    def test_body_temperature(self):
        result = self.mod.celsius_to_fahrenheit(37)
        assert abs(result - 98.6) < 0.01

    def test_negative_celsius(self):
        assert self.mod.celsius_to_fahrenheit(-10) == 14.0


# ============ TESTS PARA caller.py (P13) ============
class TestCaller:
    def test_basic_output(self):
        output = run_program("caller.py", ["5", "2.0"])
        assert "1.0" in output

    def test_zero_inputs(self):
        output = run_program("caller.py", ["0", "0.0"])
        assert "0.0" in output

    def test_larger_inputs(self):
        output = run_program("caller.py", ["10", "3.5"])
        assert "3.5" in output

    def test_output_is_float_format(self):
        output = run_program("caller.py", ["1", "1.0"])
        assert "0.1" in output

    def test_returns_a_number(self):
        output = run_program("caller.py", ["5", "2.0"])
        result = output.strip().split("\n")[-1]
        float(result)  # Debe poder convertirse a float sin error


# ============ TESTS PARA utils_calc.py + main.py (P10) ============
class TestUtilsCalc:
    def setup_method(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location("utils_calc", "utils_calc.py")
        self.mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.mod)

    def test_add_integers(self):
        assert self.mod.add(3, 5) == 8

    def test_add_float(self):
        assert self.mod.add(3.5, 5) == 8.5

    def test_sub_integers(self):
        assert self.mod.sub(10, 4) == 6

    def test_sub_float(self):
        assert self.mod.sub(10.0, 4.5) == 5.5

    def test_multiply_integers(self):
        assert self.mod.multiply(3, 4) == 12

    def test_multiply_float(self):
        assert self.mod.multiply(3.5, 4) == 14.0

    def test_divide_basic(self):
        assert self.mod.divide(10, 2) == 5.0

    def test_divide_returns_float(self):
        assert isinstance(self.mod.divide(10, 2), float)

    def test_divide_by_zero(self):
        assert self.mod.divide(4, 0) == "Error: Division by zero is not allowed."

    def test_exponent_integers(self):
        assert self.mod.exponent(2, 3) == 8

    def test_exponent_float(self):
        assert self.mod.exponent(2.0, 3) == 8.0

    def test_modulo_basic(self):
        assert self.mod.modulo(10, 3) == 1

    def test_modulo_float(self):
        assert self.mod.modulo(10.5, 3) == 1.5

    def test_modulo_by_zero(self):
        assert self.mod.modulo(10, 0) == "Error: Modulo by zero is not allowed."

    def test_floor_divide_integers(self):
        assert self.mod.floor_divide(10, 3) == 3

    def test_floor_divide_float(self):
        assert self.mod.floor_divide(10.5, 3) == 3.0

    def test_floor_divide_by_zero(self):
        assert self.mod.floor_divide(5, 0) == "Error: Division by zero is not allowed."

    def test_absolute_negative_int(self):
        assert self.mod.absolute(-5) == 5

    def test_absolute_negative_float(self):
        assert self.mod.absolute(-5.5) == 5.5

    def test_absolute_positive(self):
        assert self.mod.absolute(3) == 3


class TestMainCalculator:
    def test_add_operation(self):
        output = run_program("main.py", ["add", "3", "5", "exit"])
        assert "The result is: 8" in output

    def test_subtract_operation(self):
        output = run_program("main.py", ["subtract", "8.5", "4", "exit"])
        assert "The result is: 4.5" in output

    def test_divide_by_zero(self):
        output = run_program("main.py", ["divide", "10", "0", "exit"])
        assert "Error: Division by zero is not allowed." in output

    def test_exponent_operation(self):
        output = run_program("main.py", ["exponent", "3", "2", "exit"])
        assert "The result is: 9" in output

    def test_modulo_operation(self):
        output = run_program("main.py", ["modulo", "9", "4", "exit"])
        assert "The result is: 1" in output

    def test_absolute_operation(self):
        output = run_program("main.py", ["absolute", "-9", "exit"])
        assert "The result is: 9" in output

    def test_invalid_option(self):
        output = run_program("main.py", ["potencia", "add", "1", "1", "exit"])
        assert "Invalid option!" in output

    def test_case_insensitive(self):
        output = run_program("main.py", ["ADD", "2", "3", "exit"])
        assert "The result is: 5" in output

    def test_exit_works(self):
        output = run_program("main.py", ["exit"])
        assert "Invalid" not in output

    def test_multiply_operation(self):
        output = run_program("main.py", ["multiply", "4", "5", "exit"])
        assert "The result is: 20" in output

    def test_floor_divide_operation(self):
        output = run_program("main.py", ["floor_divide", "10", "3", "exit"])
        assert "The result is: 3" in output

    def test_modulo_by_zero(self):
        output = run_program("main.py", ["modulo", "5", "0", "exit"])
        assert "Error: Modulo by zero is not allowed." in output


# FREEZE CODE END

if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])

