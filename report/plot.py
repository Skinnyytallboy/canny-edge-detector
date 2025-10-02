from meth_sols import MathematicalProblems

try:
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
except ImportError:
    print("Error: matplotlib is required for plotting")
    print("Install it with: pip install matplotlib")
    exit(1)

def plot_1d_gaussians():
    math_prob = MathematicalProblems()
    results = math_prob.problem1_gaussian_derivatives(sigma=1.0, size=10)
    data_1d = results['1d']
    
    fig, axes = plt.subplots(3, 1, figsize=(12, 10))
    
    axes[0].plot(data_1d['x'], data_1d['G'], 'b-', linewidth=2)
    axes[0].set_title('1D Gaussian G(x)', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('x')
    axes[0].set_ylabel('G(x)')
    axes[0].grid(True, alpha=0.3)
    
    axes[1].plot(data_1d['x'], data_1d['dG_dx'], 'r-', linewidth=2)
    axes[1].set_title('First Derivative dG/dx', fontsize=14, fontweight='bold')
    axes[1].set_xlabel('x')
    axes[1].set_ylabel('dG/dx')
    axes[1].grid(True, alpha=0.3)
    axes[1].axhline(y=0, color='k', linestyle='--', alpha=0.3)
    
    axes[2].plot(data_1d['x'], data_1d['d2G_dx2'], 'g-', linewidth=2)
    axes[2].set_title('Second Derivative d²G/dx²', fontsize=14, fontweight='bold')
    axes[2].set_xlabel('x')
    axes[2].set_ylabel('d²G/dx²')
    axes[2].grid(True, alpha=0.3)
    axes[2].axhline(y=0, color='k', linestyle='--', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('gaussian_derivatives_1d.png', dpi=300, bbox_inches='tight')
    print("Saved: gaussian_derivatives_1d.png")
    plt.show()

def plot_2d_gaussians():
    math_prob = MathematicalProblems()
    results = math_prob.problem1_gaussian_derivatives(sigma=1.0, size=6)
    data_2d = results['2d']
    fig = plt.figure(figsize=(18, 12))
    
    ax1 = fig.add_subplot(2, 3, 1, projection='3d')
    ax1.plot_surface(data_2d['X'], data_2d['Y'], data_2d['G'], cmap='viridis', alpha=0.9)
    ax1.set_title('2D Gaussian G(x,y)', fontsize=12, fontweight='bold')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_zlabel('G(x,y)')
    
    ax2 = fig.add_subplot(2, 3, 2, projection='3d')
    ax2.plot_surface(data_2d['X'], data_2d['Y'], data_2d['dG_dx'], cmap='coolwarm', alpha=0.9)
    ax2.set_title('First Derivative ∂G/∂x', fontsize=12, fontweight='bold')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.set_zlabel('∂G/∂x')
    
    ax3 = fig.add_subplot(2, 3, 3, projection='3d')
    ax3.plot_surface(data_2d['X'], data_2d['Y'], data_2d['dG_dy'], cmap='coolwarm', alpha=0.9)
    ax3.set_title('First Derivative ∂G/∂y', fontsize=12, fontweight='bold')
    ax3.set_xlabel('x')
    ax3.set_ylabel('y')
    ax3.set_zlabel('∂G/∂y')
    
    ax4 = fig.add_subplot(2, 3, 5, projection='3d')
    ax4.plot_surface(data_2d['X'], data_2d['Y'], data_2d['d2G_dx2'], cmap='plasma', alpha=0.9)
    ax4.set_title('Second Derivative ∂²G/∂x²', fontsize=12, fontweight='bold')
    ax4.set_xlabel('x')
    ax4.set_ylabel('y')
    ax4.set_zlabel('∂²G/∂x²')
    
    ax5 = fig.add_subplot(2, 3, 6, projection='3d')
    ax5.plot_surface(data_2d['X'], data_2d['Y'], data_2d['d2G_dy2'], cmap='plasma', alpha=0.9)
    ax5.set_title('Second Derivative ∂²G/∂y²', fontsize=12, fontweight='bold')
    ax5.set_xlabel('x')
    ax5.set_ylabel('y')
    ax5.set_zlabel('∂²G/∂y²')
    plt.tight_layout()
    plt.savefig('gaussian_derivatives_2d.png', dpi=300, bbox_inches='tight')
    print("Saved: gaussian_derivatives_2d.png")
    plt.show()

def plot_contours():
    math_prob = MathematicalProblems()
    results = math_prob.problem1_gaussian_derivatives(sigma=1.0, size=6)
    data_2d = results['2d']
    
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    
    cs1 = axes[0, 0].contourf(data_2d['X'], data_2d['Y'], data_2d['G'], levels=20, cmap='viridis')
    axes[0, 0].set_title('2D Gaussian G(x,y)', fontsize=12, fontweight='bold')
    axes[0, 0].set_xlabel('x')
    axes[0, 0].set_ylabel('y')
    plt.colorbar(cs1, ax=axes[0, 0])
    
    cs2 = axes[0, 1].contourf(data_2d['X'], data_2d['Y'], data_2d['dG_dx'], levels=20, cmap='coolwarm')
    axes[0, 1].set_title('∂G/∂x', fontsize=12, fontweight='bold')
    axes[0, 1].set_xlabel('x')
    axes[0, 1].set_ylabel('y')
    plt.colorbar(cs2, ax=axes[0, 1])
    
    cs3 = axes[0, 2].contourf(data_2d['X'], data_2d['Y'], data_2d['dG_dy'], levels=20, cmap='coolwarm')
    axes[0, 2].set_title('∂G/∂y', fontsize=12, fontweight='bold')
    axes[0, 2].set_xlabel('x')
    axes[0, 2].set_ylabel('y')
    plt.colorbar(cs3, ax=axes[0, 2])
    
    cs4 = axes[1, 1].contourf(data_2d['X'], data_2d['Y'], data_2d['d2G_dx2'], levels=20, cmap='plasma')
    axes[1, 1].set_title('∂²G/∂x²', fontsize=12, fontweight='bold')
    axes[1, 1].set_xlabel('x')
    axes[1, 1].set_ylabel('y')
    plt.colorbar(cs4, ax=axes[1, 1])
    
    cs5 = axes[1, 2].contourf(data_2d['X'], data_2d['Y'], data_2d['d2G_dy2'], levels=20, cmap='plasma')
    axes[1, 2].set_title('∂²G/∂y²', fontsize=12, fontweight='bold')
    axes[1, 2].set_xlabel('x')
    axes[1, 2].set_ylabel('y')
    plt.colorbar(cs5, ax=axes[1, 2])
    axes[1, 0].axis('off')
    
    plt.tight_layout()
    plt.savefig('gaussian_derivatives_contours.png', dpi=300, bbox_inches='tight')
    print("Saved: gaussian_derivatives_contours.png")
    plt.show()

if __name__ == "__main__":
    print("Generating plots for Problem 1: Gaussian Derivatives\n")
    print("Plotting 1D Gaussians...")
    plot_1d_gaussians()
    print("\nPlotting 2D Gaussians (surface plots)...")
    plot_2d_gaussians()
    print("\nPlotting 2D Gaussians (contour plots)...")
    plot_contours()
    print("\nAll plots generated successfully!")
    print("Include these images in your mathematicalPart.pdf")