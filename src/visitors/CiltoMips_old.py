from utils.mip_utils import registers, operations, datatype
import visitors.visitor as visitor
from cil_ast.cil_ast import *

class CiltoMipsVisitor:
    def __init__(self, context):
        self.dottypes = []
        self.dotdata =[]
        self.dotcode =[]
        self.context = context
        self.code = []
        self.data = []
    def write_data(self, instruction):
        self.data.append(instruction)

    def write_code(self, instruction):
        self.code.append(instruction)
        
        

    @visitor.on('node')
    def visit(self, node):
        pass

    @visitor.when(ProgramNode)
    def visit(self, node):
        self.dottypes = node.dottypes
        self.dotdata = node.dotdata
        self.dotcode = node.dotcode

        self.write_data('.data')
        self.write_code('.text')

        inherited = "# Inherited Method\n" \
                     ".inherited:\n" \
                     "lw $a0, 8($sp)\n" \
                     "lw $a1, 4($sp)\n" \
                     "lw $a0, ($a0)\n" \
                     "lw $a2, ($a0)\n" \
                     "lw $a3, 4($a0)\n" \
                     "lw $a0, ($a1)\n" \
                     "lw $a1, 4($a1)\n" \
                     "sge $t0, $a2, $a0\n" \
                     "sle $t1, $a3, $a1\n" \
                     "and $a0, $t0, $t1\n" \
                     "sw $a0, ($sp)\n" \
                     "subu $sp, $sp, 4\n" \
                     "jr $ra\n" \
                     "\n"

        raise_exc = "# raise exception Method\n" \
                    ".raise:\n" \
                    "lw $a0, 4($sp)\n" \
                    "li $v0, 4\n" \
                    "syscall\n" \
                    "li $v0, 10\n" \
                    "syscall"

        self.write_data("# Start .data segment (data!)")
        self.write_data(".data")
        self.write_data("zero_error: .asciiz \"Divition by zero exception\"")
        self.write_data("index_error: .asciiz \"Invalid index exception\"")
        self.write_data("void_error: .asciiz \"Objects must be inizializated before use exception\"")
        self.write_data("case_error: .asciiz \"Case expression no match exception\"")
        self.write_data("void_str: .asciiz \"\"")
        
        self.write_code(inherited)
        self.write_code(raise_exc)
        
        self.write_code("main:")
        self.write_code(f'{operations.move} {registers.s7} {registers.gp}')
        self.write_code(f'{operations.addi} {registers.s7} {registers.s7} 300000')
        self.write_code(f"")
        
        self.write_data(f"_abort: {datatype.asciiz} \"Program Aborted\"")
        self.write_data(f"_zero: {datatype.asciiz} \"0 Division Error\"")
        self.write_data(f"_substr: {datatype.asciiz} \"Substr Length Error\"")
        self.write_data(f"_mem: {datatype.asciiz} \"Memory Error\"")
        self.write_data(f"")

        for i, d in enumerate(self.dotdata):
            self.write_data("msg{}: {} \"{}\"".format(i, datatype.asciiz, d))   # every one of the user defined data through the program
        
        self.write_data('buffer: .space 1024')  # buffer for the in_string method

        for i, t in enumerate(self.dottypes):
            self.write_data(f"type_str{i}: {datatype.asciiz} \"{t.name}\"")
        
        for i, t in enumerate(self.dottypes):
            # words = f"{tipe.cType}: .word {tipe.t_in}, {tipe.t_out}, type_str{i}"
            words = f"{t.name}: .word 12, 42, type_str{i}"
            for method in t.methods:
                words += ", " + "." + method[1]
            self.write_data(words)

        for instr in self.dotcode:
            a = 0


    @visitor.when(TypeNode)
    def visit(self, node):
        pass

    @visitor.when(DataNode)
    def visit(self, node):
        pass

    @visitor.when(FunctionNode)
    def visit(self, node):
        methods = [
            'Object_abort',
            'Object_type_name',
            'Object_copy',
            'String_concat',
            'String_substr',
            'String_length',
            'IO_in_int',
            'IO_out_int',
            'IO_in_string',
            'IO_out_string',
        ]
        if node.fname in methods: 
            return
        pass
    
    @visitor.when(ParamNode)
    def visit(self, node):
        pass

    @visitor.when(LocalNode)
    def visit(self, node):
        pass

    @visitor.when(AssignNode)
    def visit(self, node):
        pass

    @visitor.when(PlusNode)
    def visit(self, node):
        pass
        
    @visitor.when(MinusNode)
    def visit(self, node):
        pass

    @visitor.when(StarNode)
    def visit(self, node):
        pass

    @visitor.when(DivNode)
    def visit(self, node):
        pass

    @visitor.when(EqualNode)
    def visit(self, node):
        pass

    @visitor.when(LessNode)
    def visit(self, node):
        pass

    @visitor.when(LeqNode)
    def visit(self, node):
        pass

    @visitor.when(GotoNode)
    def visit(self, node):
        pass

    @visitor.when(GotoIfNode)
    def visit(self, node):
        pass

    @visitor.when(GetAttribNode)
    def visit(self, node):
        pass

    @visitor.when(SetAttribNode)
    def visit(self, node):
        pass

    @visitor.when(AllocateNode)
    def visit(self, node):
        pass

    @visitor.when(TypeOfNode)
    def visit(self, node):
        pass

    @visitor.when(LabelNode)
    def visit(self, node):
        pass

    @visitor.when(IsTypeNode)
    def visit(self, node):
        pass

    @visitor.when(ParentTypeNode)
    def visit(self, node):
        pass

    @visitor.when(StaticCallNode)
    def visit(self, node):
        pass

    @visitor.when(DynamicCallNode)
    def visit(self, node):
        pass
    
    @visitor.when(ArgNode)
    def visit(self, node):
        pass

    @visitor.when(ReturnNode)
    def visit(self, node):
        pass

    @visitor.when(LoadNode)
    def visit(self, node):
        pass

    @visitor.when(LengthNode)
    def visit(self, node):
        pass

    @visitor.when(ConcatNode)
    def visit(self, node):
        pass

    @visitor.when(PrefixNode)
    def visit(self, node):
        pass

    @visitor.when(SubstringNode)
    def visit(self, node):
        pass

    @visitor.when(ToStrNode)
    def visit(self, node):
        pass

# Input espacio a reservar en $a0
# Output direccion de memoria reservada en $a0
    def mem_alloc(self):
        self.write_code(f"# Declartation of the mem_alloc")

        self.write_code(f"mem_alloc:")
        self.write_code(f"{operations.add} {registers.gp} {registers.gp} {registers.a0}")
        self.write_code(f"{operations.blt} {registers.gp} {registers.s7} mem_alloc_end")# si se pasa del límite de memoria dar error
        self.write_code(f"{operations.j} mem_error")
        self.write_code(f"mem_alloc_end:")
        self.write_code(f"{operations.sub} {registers.a0} {registers.gp} {registers.a0}")    
        self.write_code(f"{operations.jr} {registers.ra}")
        self.write_code(f"")

# en a0 tengo el la instancia
    def get_parent_prot(self):
        self.write_code(f"# get parent prototype") #
        self.write_code(f"get_parent_prot:")
        self.write_code(f"{operations.lw} {registers.t0} ({registers.a0})")
        self.write_code(f"{operations.sll} {registers.t0} {registers.t0} 2")# mult por 4 pa tener el offset
        self.write_code(f"{operations.lw} {registers.t0} ({registers.s4})")
        self.write_code(f"{operations.move} {registers.a0} {registers.t0}")
        self.write_code(f"{operations.jr} {registers.ra}")
        self.write_code(f"")

# funciones para errores en runtime
    def zero_error(self): # error al dividir por 0
        self.write_code(f"# Declartation of the zero-div runtime error")

        self.write_code(f"zero_error:")
        self.write_code(f"{operations.la} {registers.a0} _zero")
        self.write_code(f"")

        self.write_code(f"{operations.li} {registers.v0} 4")
        self.write_code(f"{operations.syscall}")
        self.write_code(f"{operations.li} {registers.v0} 10")
        self.write_code(f"{operations.syscall}")
        self.write_code(f"")

    def substr_error(self):
        self.write_code(f"# Declartation of the substr-index.out.of.range runtime error")

        self.write_code(f"substr_error:")
        self.write_code(f"{operations.la} {registers.a0} _substr")
        self.write_code(f"")
        
        self.write_code(f"{operations.li} {registers.v0} 4")
        self.write_code(f"{operations.syscall}")
        self.write_code(f"{operations.li} {registers.v0} 10")
        self.write_code(f"{operations.syscall}")
        self.write_code(f"")
    
    def mem_error(self):
        self.write_code(f"# Declartation of the memory-overflow runtime error")
        self.write_code(f"mem_error:")
        self.write_code(f"{operations.la} {registers.a0} _mem")
        self.write_code(f"")
        
        self.write_code(f"{operations.li} {registers.v0} 4")
        self.write_code(f"{operations.syscall}")
        self.write_code(f"{operations.li} {registers.v0} 10")
        self.write_code(f"{operations.syscall}")
        self.write_code(f"")


    def utils_functs(self):
        self.mem_alloc()
        self.get_parent_prot()
        self.object_copy()
        self.str_eq()
        self.str_concat()
        self.str_substr()
        self.length()
        self.zero_error()
        self.mem_error()
        self.substr_error()