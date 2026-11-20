import math

def bounds_union(a, b):
    """合并两个包围盒。"""
    raise NotImplementedError("TODO: bounds_union")

def node_is_leaf(count, max_leaf):
    """叶子判定。"""
    raise NotImplementedError("TODO: node_is_leaf")

def refit_threshold(overlap, triangle_count):
    """refit 或 rebuild。"""
    raise NotImplementedError("TODO: refit_threshold")

def update_ancestors(path):
    """祖先路径去重。"""
    raise NotImplementedError("TODO: update_ancestors")

def instance_mask(material_mask, layer_mask):
    """实例掩码。"""
    raise NotImplementedError("TODO: instance_mask")

def traversal_stack_limit(depth, base):
    """遍历栈容量。"""
    raise NotImplementedError("TODO: traversal_stack_limit")

def node_pool_reclaim(used, freed):
    """节点池回收。"""
    raise NotImplementedError("TODO: node_pool_reclaim")

def blas_double_buffer(active, next_buffer):
    """BLAS 双缓冲切换。"""
    raise NotImplementedError("TODO: blas_double_buffer")

def fence_required(producer, consumer):
    """跨队列同步。"""
    raise NotImplementedError("TODO: fence_required")

def frame_align(bvh_frame, camera_frame):
    """BVH 与相机对齐。"""
    raise NotImplementedError("TODO: frame_align")

def instance_key(instance_id, blas_id):
    """实例唯一键。"""
    raise NotImplementedError("TODO: instance_key")

def leaf_capacity(triangles, max_leaf):
    """叶子容量。"""
    raise NotImplementedError("TODO: leaf_capacity")

def box_overlap(a, b):
    """包围盒相交。"""
    raise NotImplementedError("TODO: box_overlap")

def refit_root(child_bounds):
    """根节点 refit。"""
    raise NotImplementedError("TODO: refit_root")

def tlas_rebuild_needed(added, removed, moved):
    """TLAS 重建判定。"""
    raise NotImplementedError("TODO: tlas_rebuild_needed")
