#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Neg.py
@time: 2019/9/15 20:01
@desc: 取反(neg)指令
"""
from instructions.base.Instruction import NoOperandsInstruction


def _neg(frame):
    stack = frame.operand_stack
    val = stack.pop_numeric()
    stack.push_numeric(-val)


# double negate
class DNEG(NoOperandsInstruction):
    def execute(self, frame):
        _neg(frame)


# float negate
class FNEG(NoOperandsInstruction):
    def execute(self, frame):
        _neg(frame)


# int negate
class INEG(NoOperandsInstruction):
    def execute(self, frame):
        _neg(frame)


# long negate
class LNEG(NoOperandsInstruction):
    def execute(self, frame):
        _neg(frame)
