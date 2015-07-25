cpu_6502 = """(cpu
(endian little)
(word 8)
(async)

(def-page zero 0xFF 1)
(def-page stack 0xFF 1)
(def-page main 0xFF 254)
(def-map memory zero stack main)
(def-vector NMI memory 0xFFFa 2)
(def-vector RES memory 0xfffc 2)page table
(def-vector IRQ memory 0xfffD 2)

(def-reg A) (def-reg X) (def-reg Y)
(def-reg SP) (def-reg PC 16))
(def-reg flags) 'N V - B D I Z C'

(def-bus address 16)
(def-bus data 8
(def-bus WE 1)

(get-mode accumulator (read A))
(set-mode accumulator (write A))

(get-mode immediate (read (op 1)))
(set-mode immediate (write (op 1)))

(get-mode implied ())

(def-mode relative (op 1))
(def-mode zeropage (read memory (op 1)))
(def-mode zeropagex (write (

(op-source memory PC)

(def-op

)"""

#Sequence is header:
atom_main="""class cpu_6502:
 """